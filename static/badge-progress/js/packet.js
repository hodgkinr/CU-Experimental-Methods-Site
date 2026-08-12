export function base64UrlToBytes(value) {
  const normalized = value.replace(/-/g, "+").replace(/_/g, "/");
  const padded = normalized.padEnd(Math.ceil(normalized.length / 4) * 4, "=");
  const binary = atob(padded);
  return Uint8Array.from(binary, (char) => char.charCodeAt(0));
}

export function bytesToUtf8(bytes) {
  return new TextDecoder().decode(bytes);
}

export function canonicalJson(value) {
  if (value === null || typeof value !== "object") {
    return JSON.stringify(value);
  }
  if (Array.isArray(value)) {
    return `[${value.map((item) => canonicalJson(item)).join(",")}]`;
  }
  return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`).join(",")}}`;
}

export function decodeProgressCode(code) {
  const compact = code.trim();
  if (!compact) {
    throw new Error("Progress code is empty.");
  }
  const envelope = JSON.parse(bytesToUtf8(base64UrlToBytes(compact)));
  if (!envelope.payload || !envelope.signature) {
    throw new Error("Progress code is missing packet fields.");
  }
  return envelope;
}

export function summarizePacket(packet, courseModel) {
  const latest = packet.events.at(-1);
  const subCLOCount = courseModel.clos.reduce((sum, clo) => sum + clo.subCLOs.length, 0);
  return {
    eventCount: packet.events.length,
    latestLabel: latest?.eventLabel || "Current",
    subCLOCount,
    assessmentCount: courseModel.majorAssessments.length
  };
}

export function validatePacket(packet, courseModel) {
  if (packet.schema !== courseModel.packet.schema || packet.version !== courseModel.packet.version) {
    throw new Error("Progress packet schema is not supported by this prototype.");
  }
  if (!packet.nonce || typeof packet.nonce !== "string") {
    throw new Error("Progress packet is missing its nonce.");
  }
  if (!Array.isArray(packet.events) || packet.events.length === 0) {
    throw new Error("Progress packet does not contain any progress events.");
  }
  const knownSubCLOs = new Set(courseModel.clos.flatMap((clo) => clo.subCLOs.map((sub) => sub.id)));
  const knownAssessments = new Set(courseModel.majorAssessments.map((assessment) => assessment.id));

  packet.events.forEach((event) => {
    if (!event.subCLOStates || !event.majorAssessmentStates) {
      throw new Error("Progress event is missing state data.");
    }
    Object.entries(event.subCLOStates).forEach(([id, state]) => {
      if (!knownSubCLOs.has(id)) {
        throw new Error(`Progress packet references unknown sub-CLO: ${id}`);
      }
      if (!Number.isInteger(state) || state < 0 || state > 3) {
        throw new Error(`Invalid state for ${id}.`);
      }
    });
    Object.entries(event.majorAssessmentStates).forEach(([id, state]) => {
      if (!knownAssessments.has(id)) {
        throw new Error(`Progress packet references unknown assessment: ${id}`);
      }
      if (state !== 0 && state !== 1) {
        throw new Error(`Invalid pass/fail state for ${id}.`);
      }
    });
  });
}

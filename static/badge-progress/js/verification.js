import { base64UrlToBytes, canonicalJson } from "./packet.js";

export const PUBLIC_KEY_JWK = Object.freeze({
  "crv": "P-256",
  "ext": true,
  "key_ops": ["verify"],
  "kty": "EC",
  "x": "7uBu72QbbJLTTSAjlY2bWA1BflFCpIeMORnLwmHr7LM",
  "y": "3ABzhMYlG3n_Roamhms473YGGO-moJdtfNApcifmcnc"
});

const SIGNATURE_ALGORITHM = Object.freeze({
  name: "ECDSA",
  namedCurve: "P-256",
  hash: "SHA-256"
});

let importedPublicKey;

export async function verifyEnvelope(envelope) {
  importedPublicKey ||= await crypto.subtle.importKey(
    "jwk",
    PUBLIC_KEY_JWK,
    SIGNATURE_ALGORITHM,
    false,
    ["verify"]
  );
  const payloadBytes = new TextEncoder().encode(canonicalJson(envelope.payload));
  const signatureBytes = base64UrlToBytes(envelope.signature);
  return crypto.subtle.verify(SIGNATURE_ALGORITHM, importedPublicKey, signatureBytes, payloadBytes);
}

export const PROTOTYPE_STATE_LEVELS = Object.freeze({
  0: { label: "Insufficient Evidence", shortLabel: "Insufficient" },
  1: { label: "Developing", shortLabel: "Developing" },
  2: { label: "Proficient", shortLabel: "Proficient" },
  3: { label: "Mastery", shortLabel: "Mastery" }
});

export const COURSE_CONFIG = Object.freeze({
  schemaVersion: "asen3501-badge-config-v1",
  course: {
    id: "ASEN 3501",
    title: "Aerospace Experimental Methods"
  },
  sourceOfTruthPath: "./badge-progress/data/clo_source_of_truth.json",
  badgeAssetBasePath: "./badge-progress/assets/badges",
  badgeAssetExtension: "png",
  majorAssessments: [
    { id: "lab1", label: "Lab 1" },
    { id: "tier1", label: "Tier 1" },
    { id: "tier2", label: "Tier 2" },
    { id: "final_project", label: "Final Project" },
    { id: "in_class_exam", label: "In-class Exam" }
  ],
  packet: {
    schema: "asen3501-progress-packet",
    version: 1,
    signatureAlgorithm: "ECDSA-P256-SHA256"
  }
});

export async function loadCourseModel() {
  const response = await fetch(COURSE_CONFIG.sourceOfTruthPath, { cache: "no-store" });
  if (!response.ok) {
    throw new Error(`Unable to load CLO source of truth: ${response.status}`);
  }
  const source = await response.json();
  const clos = source.clos.map((clo) => ({
    id: clo.id,
    title: clo.title,
    statement: clo.statement,
    badgeImage: `${COURSE_CONFIG.badgeAssetBasePath}/${clo.id}.png`,
    subCLOs: clo.sub_clos.map((sub) => ({
      id: sub.id,
      title: sub.title,
      description: sub.description
    }))
  }));

  return {
    ...COURSE_CONFIG,
    sourceSchemaVersion: source.schema_version,
    clos
  };
}

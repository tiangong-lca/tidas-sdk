export type ValidationSeverity = 'error' | 'warning' | 'info';

export interface ValidationIssue {
  issue_code: string;
  severity: ValidationSeverity;
  category: string;
  file_path: string;
  message: string;
  location: string;
  context: Record<string, unknown>;
}

export interface ValidationSummary {
  issue_count: number;
  error_count: number;
  warning_count: number;
  info_count: number;
}

export interface CategoryValidationReport {
  category: string;
  ok: boolean;
  summary: ValidationSummary;
  issues: ValidationIssue[];
}

export interface PackageValidationSummary extends ValidationSummary {
  category_count: number;
}

export interface PackageValidationReport {
  input_dir: string;
  ok: boolean;
  summary: PackageValidationSummary;
  categories: CategoryValidationReport[];
  issues: ValidationIssue[];
}

export function summarizeIssues(issues: ValidationIssue[]): ValidationSummary {
  const errorCount = issues.filter(
    (issue) => issue.severity === 'error'
  ).length;
  const warningCount = issues.filter(
    (issue) => issue.severity === 'warning'
  ).length;
  const infoCount = issues.filter((issue) => issue.severity === 'info').length;

  return {
    issue_count: issues.length,
    error_count: errorCount,
    warning_count: warningCount,
    info_count: infoCount,
  };
}

export function buildCategoryReport(
  category: string,
  issues: ValidationIssue[]
): CategoryValidationReport {
  return {
    category,
    ok: issues.length === 0,
    summary: summarizeIssues(issues),
    issues,
  };
}

export function buildPackageReport(
  inputDir: string,
  categoryReports: CategoryValidationReport[]
): PackageValidationReport {
  const issues = categoryReports.flatMap((report) => report.issues);
  const summary = summarizeIssues(issues);

  return {
    input_dir: inputDir,
    ok: issues.length === 0,
    summary: {
      category_count: categoryReports.length,
      ...summary,
    },
    categories: categoryReports,
    issues,
  };
}

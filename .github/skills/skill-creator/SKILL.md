---
name: skill-creator
version: 1.0.0
description: Create, test, and validate domain-specific skills with comprehensive context, responsibility definitions, input specifications, structured processes, validation logic, and dynamic test suites with assertions.
tags: [skill-generation, testing, validation, automation]
---

# Skill Creator

## Overview

The skill-creator skill provides a structured framework for creating, testing, and validating reusable domain-specific skills. It ensures every skill is properly documented, thoroughly tested, and meets quality standards.

## Context & Responsibility

### Context
- **Domain**: Skill authoring and quality assurance
- **Target Users**: Engineers, domain experts, AI agent trainers
- **Scope**: Creation of domain-specific knowledge packages that enhance agent capabilities
- **Integration**: Works with VS Code extension ecosystem and Copilot agent customization

### Responsibility
- Define clear skill structure and metadata
- Establish testing and validation mechanisms
- Ensure skills are self-documenting and maintainable
- Validate skill functionality against test cases before deployment
- Generate skill quality reports and metrics

## Required Inputs

### Core Inputs
1. **Skill Metadata**
   - `name` (string): Unique identifier (kebab-case)
   - `description` (string): 1-2 sentence purpose statement
   - `domain` (string): Primary problem domain
   - `version` (string): Semantic version (e.g., 1.0.0)
   - `tags` (array): Categorization tags

2. **Skill Definition**
   - `context` (object): Context where skill applies
     - `domain`: Problem area
     - `target_users`: Who uses this skill
     - `scope`: Boundaries of applicability
   - `responsibility` (object): What the skill does
     - `primary_goal`: Main objective
     - `constraints`: Limitations and boundaries
     - `success_criteria`: Measurable outcomes
   - `required_inputs` (array): Data/parameters needed
     - `name`, `type`, `description`, `required` (boolean)
   - `outputs` (array): Results produced
     - `name`, `type`, `description`

3. **Process Definition**
   - `main_process` (string): High-level workflow description
   - `steps` (array): Detailed procedural steps
     - `id`: Step identifier
     - `description`: What happens
     - `action`: Implementation details
     - `conditions`: Entry conditions
     - `next_steps`: Conditional branching
   - `validation_rules` (array): Rules to validate results
     - `rule_id`, `condition`, `error_message`, `severity`

4. **Test Suite**
   - `test_cases` (array): Input-output test pairs
     - `id`: Test identifier
     - `description`: What is being tested
     - `input`: Sample data
     - `expected_output`: Expected result
     - `assertions` (array): Validation checks
   - `edge_cases` (array): Boundary condition tests
   - `error_cases` (array): Failure scenario tests

## Main Process

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. SKILL DEFINITION                                             │
│    ├─ Collect metadata                                          │
│    ├─ Define context & responsibility                           │
│    └─ Specify inputs/outputs                                    │
├─────────────────────────────────────────────────────────────────┤
│ 2. PROCESS MAPPING                                              │
│    ├─ Document main workflow                                    │
│    ├─ Break down into steps                                     │
│    ├─ Define step conditions & transitions                      │
│    └─ Establish validation rules                                │
├─────────────────────────────────────────────────────────────────┤
│ 3. TEST CREATION                                                │
│    ├─ Generate test cases with sample data                      │
│    ├─ Define assertions for each test                           │
│    ├─ Create edge case tests                                    │
│    └─ Create error scenario tests                               │
├─────────────────────────────────────────────────────────────────┤
│ 4. DYNAMIC TESTING                                              │
│    ├─ Execute test suite against skill                          │
│    ├─ Validate outputs against assertions                       │
│    ├─ Generate test report with pass/fail metrics               │
│    └─ Collect coverage metrics                                  │
├─────────────────────────────────────────────────────────────────┤
│ 5. VALIDATION & QUALITY CHECKS                                  │
│    ├─ Verify all inputs are handled                             │
│    ├─ Validate output format consistency                        │
│    ├─ Check error handling coverage                             │
│    ├─ Review documentation completeness                         │
│    └─ Generate quality score                                    │
├─────────────────────────────────────────────────────────────────┤
│ 6. SKILL DEPLOYMENT                                             │
│    ├─ Create SKILL.md file with full documentation              │
│    ├─ Include YAML frontmatter                                  │
│    ├─ Attach test suite for CI/CD integration                   │
│    └─ Generate quality report                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Process Steps

### Step 1: Collect Skill Metadata
**ID**: `skill-meta-001`

**Conditions to Enter**:
- User provides skill name and domain
- Description of intended skill is available
- Target use cases identified

**Actions**:
```
1. Validate skill name format (kebab-case, 3-20 chars)
2. Extract domain and categorize
3. Define version (default: 1.0.0)
4. Assign tags for discoverability
5. Store metadata in skill registry
```

**Next Steps**:
- ✅ Continue → Step 2 (if all metadata provided)
- ⚠️ Clarify → Ask user for missing information
- ❌ Stop → Reject if critical fields missing

---

### Step 2: Define Context & Responsibility
**ID**: `skill-context-002`

**Conditions to Enter**:
- Skill metadata complete
- Domain clearly understood

**Actions**:
```
1. Map skill domain to problem space
2. Identify target user profiles
3. Define scope boundaries (what's in/out)
4. State primary goal clearly
5. Document constraints and limitations
6. Establish success criteria (measurable)
7. List any dependencies on other skills
```

**Next Steps**:
- ✅ Continue → Step 3 (if context clear)
- ⚠️ Refine → Clarify constraints or scope
- ❌ Conflict → Alert if conflicts with existing skills

---

### Step 3: Specify Inputs & Outputs
**ID**: `skill-io-003`

**Conditions to Enter**:
- Context and responsibility defined
- Skill purpose understood

**Actions**:
```
1. List all required inputs with types
   - Primitive types (string, number, boolean)
   - Complex types (object, array)
   - Enum options if applicable
2. Define output structure
3. Specify optional vs required fields
4. Document default values
5. Create input validation rules
   - Type checking
   - Range constraints
   - Pattern matching (regex)
6. Create output format specification
```

**Next Steps**:
- ✅ Continue → Step 4 (if I/O specification complete)
- ⚠️ Clarify → Ask for type details
- ❌ Invalid → Reject if I/O incompatible with goal

---

### Step 4: Map Process & Steps
**ID**: `skill-process-004`

**Conditions to Enter**:
- Inputs and outputs defined
- Skill workflow understood

**Actions**:
```
1. Describe high-level workflow (main_process)
2. Break workflow into discrete steps (5-15 steps)
3. For each step, document:
   a. Step ID and description
   b. Required inputs for this step
   c. Processing logic/action
   d. Entry conditions (prerequisites)
   e. Exit conditions (success/failure)
   f. Next step routing (if, else, switch)
4. Define validation rules for outputs
   a. Type validation
   b. Value range checking
   c. Consistency rules
   d. Business rule validation
5. Create step dependency graph
```

**Next Steps**:
- ✅ Continue → Step 5 (if process complete)
- ⚠️ Refine → Simplify or split steps
- ❌ Invalid → Check for circular dependencies

---

### Step 5: Design Test Suite
**ID**: `skill-tests-005`

**Conditions to Enter**:
- Process and steps fully mapped
- I/O specification complete

**Actions**:
```
1. Create "Happy Path" test cases
   - Use realistic sample data
   - Verify expected outputs
   - Define 3-5 assertions per test
2. Create edge case tests
   - Boundary value tests
   - Null/empty input tests
   - Maximum/minimum value tests
   - Special character handling
3. Create error scenario tests
   - Invalid input handling
   - Missing required fields
   - Type mismatch errors
   - Timeout/resource constraints
4. Generate test data fixtures
   - Use realistic domain data
   - Create reusable test objects
   - Mock external dependencies
5. Define assertion patterns
   - Output format validation
   - Value correctness checks
   - Business logic verification
   - Error message validation
```

**Test Assertion Format**:
```
assert {output_field} {operator} {expected_value} : "{failure_message}"
operators: ==, !=, <, >, <=, >=, matches, contains, in_range, is_null, is_not_null
```

**Next Steps**:
- ✅ Continue → Step 6 (if test suite complete)
- ⚠️ Expand → Add more edge cases
- ❌ Invalid → Fix failing assertions

---

### Step 6: Execute Dynamic Tests
**ID**: `skill-exec-006`

**Conditions to Enter**:
- Test suite defined with assertions
- Skill implementation available

**Actions**:
```
1. Initialize skill execution environment
2. For each test case:
   a. Prepare input data
   b. Execute skill with inputs
   c. Capture output and side effects
   d. Run each assertion
   e. Log pass/fail with details
3. Aggregate test results:
   - Total tests run
   - Passed/failed/skipped counts
   - Code coverage metrics
   - Performance metrics (time, memory)
4. Generate detailed test report
   a. Test summary (pass rate %)
   b. Failure analysis
   c. Coverage gaps
   d. Performance analysis
5. Identify failed test root causes
```

**Next Steps**:
- ✅ Continue → Step 7 (if all tests pass, >80% coverage)
- ⚠️ Debug → Investigate failing tests
- ❌ Halt → Fix skill implementation, re-run tests

---

### Step 7: Validate Results & Quality
**ID**: `skill-validate-007`

**Conditions to Enter**:
- All tests passing (or waived failures documented)
- Test coverage >80%

**Actions**:
```
1. Validate input handling
   - All required inputs processed
   - Optional inputs handled correctly
   - Invalid inputs caught
2. Validate output consistency
   - All outputs follow spec format
   - No unexpected side effects
   - Error responses consistent
3. Check error handling
   - All error paths tested
   - Error messages clear and actionable
   - Graceful failure modes
4. Documentation quality check
   - Context clearly stated
   - Responsibility well-defined
   - Steps documented with examples
   - Edge cases explained
5. Dependency validation
   - All external dependencies documented
   - Circular dependencies checked
   - Version constraints specified
6. Performance validation
   - Execution time acceptable
   - Memory usage within bounds
   - No resource leaks
7. Generate quality score
   - Coverage × Correctness × Documentation
   - Target: >85 quality score
```

**Validation Rules**:
```
- all_inputs_handled: count(input_tests) == count(inputs)
- output_consistency: all(output.format == spec.format)
- error_coverage: error_tests_passed >= 3
- documentation_complete: coverage([context, responsibility, steps, examples]) >= 90%
- quality_score: (coverage * 0.4 + correctness * 0.4 + documentation * 0.2) >= 85
```

**Next Steps**:
- ✅ Continue → Step 8 (if quality score ≥85, all validations pass)
- ⚠️ Improve → Address quality gaps
- ❌ Reject → Resubmit after major revisions

---

### Step 8: Generate & Deploy Skill File
**ID**: `skill-deploy-008`

**Conditions to Enter**:
- All validations passed
- Quality score ≥85
- Test suite complete

**Actions**:
```
1. Generate SKILL.md file with:
   a. YAML frontmatter (name, version, description, tags)
   b. Full skill documentation
   c. Embedded test suite (YAML block)
   d. Quick reference guide
2. Include test fixtures
   - Sample data sets
   - Expected outputs
   - Mock dependencies
3. Create CI/CD integration hooks
   - Pre-commit test runner
   - Regression test triggers
   - Quality gates
4. Generate quality report
   - Test results summary
   - Coverage breakdown
   - Performance metrics
   - Improvement recommendations
5. Create deployment package
   - Compressed skill bundle
   - Metadata and registry entry
   - Installation instructions
6. Deploy to skill registry
   - Update index
   - Version control
   - Backup previous version
```

**Skill File Template**:
```markdown
---
name: {skill_name}
version: {version}
description: {description}
domain: {domain}
tags: {tags}
quality_score: {score}
test_coverage: {coverage}%
last_updated: {timestamp}
---

# {Skill Title}

## Overview
{description}

## Context & Responsibility
[Full context and responsibility section]

## Required Inputs
[I/O specification table]

## Main Process
[Workflow diagram and description]

## Process Steps
[Detailed step-by-step breakdown]

## Test Suite
\`\`\`yaml
test_cases:
  - id: test_001
    description: {test_description}
    input: {input_data}
    expected_output: {expected}
    assertions:
      - {assertion1}
      - {assertion2}
\`\`\`

## Validation & Quality
- Test Coverage: {coverage}%
- Quality Score: {score}/100
- Last Test Run: {timestamp}
- Status: {APPROVED|NEEDS_REVIEW}
```

**Next Steps**:
- ✅ Complete → Skill deployed successfully
- ⚠️ Manual Review → Human approval required
- ❌ Error → Address deployment issues

---

## Conditions to Pass to Next Step

### Universal Transition Rules

| From Step | Condition | Action | Next Step |
|-----------|-----------|--------|-----------|
| ANY | Critical error found | Halt and report | User intervention |
| ANY | User requests clarification | Pause process | Ask clarifying questions |
| ANY | Missing required data | Halt | Request missing inputs |
| Meta → Context | ✅ All metadata valid | Continue | Context Definition |
| Context → I/O | ✅ Scope clear, goals measurable | Continue | I/O Specification |
| I/O → Process | ✅ I/O compatible with goals | Continue | Process Mapping |
| Process → Tests | ✅ Process complete, no loops | Continue | Test Suite Design |
| Tests → Exec | ✅ Test suite ready, ≥10 tests | Continue | Test Execution |
| Exec → Validate | ⚠️ 50-80% passing | Continue with warnings | Validation |
| Exec → Exec | ❌ <50% passing | Stop | Debug skill |
| Validate → Deploy | ✅ Quality ≥85, coverage ≥80% | Continue | Deployment |
| Validate → Improve | ⚠️ Quality 70-85 | Iterate | Return to relevant step |
| Validate → Reject | ❌ Quality <70 | Stop | Resubmit or abandon |

---

## Validation & Result Validation

### Automated Validation Checks

```yaml
validation_suite:
  metadata_checks:
    - skill_name_format: "^[a-z][a-z0-9-]*[a-z0-9]$"
    - version_format: "semantic"
    - required_fields: ["name", "description", "domain"]
    
  context_checks:
    - scope_defined: "required"
    - target_users_identified: "required"
    - success_criteria_measurable: "required"
    
  io_checks:
    - all_inputs_typed: "required"
    - all_outputs_specified: "required"
    - validation_rules_present: "required"
    
  process_checks:
    - no_circular_dependencies: "required"
    - all_steps_have_exit_conditions: "required"
    - complete_step_coverage: "required"
    
  test_checks:
    - minimum_test_count: 10
    - minimum_coverage: "80%"
    - all_assertions_specific: "required"
    - edge_case_tests_present: "required"
    
  quality_checks:
    - documentation_completeness: ">90%"
    - assertion_pass_rate: ">95%"
    - quality_score: ">=85"
```

### Result Validation Framework

```yaml
assert_result_structure:
  - field: "status"
    type: "enum"
    allowed: ["success", "partial", "failed"]
    assertion: 'status == "success" : "Skill execution failed"'
    
  - field: "test_results"
    type: "object"
    required_fields: ["passed", "failed", "total", "coverage"]
    assertions:
      - 'passed + failed == total : "Test count mismatch"'
      - 'coverage >= 0.8 : "Coverage below 80% threshold"'
      - 'failed == 0 : "Tests failed"'
      
  - field: "quality_metrics"
    type: "object"
    assertions:
      - 'quality_score >= 85 : "Quality score below 85"'
      - 'documentation_completeness >= 0.9 : "Documentation incomplete"'
      
  - field: "errors"
    type: "array"
    assertion: 'length == 0 : "Errors found during execution"'
```

---

## Example: Complete Skill Creation Test

### Test Case: skill-creator Self-Test

**Input:**
```json
{
  "metadata": {
    "name": "example-analyzer",
    "domain": "data-analysis",
    "description": "Analyzes data patterns and generates insights",
    "version": "1.0.0"
  },
  "context": {
    "domain": "Data analysis and pattern recognition",
    "target_users": ["Data scientists", "Analysts"],
    "scope": "Structured numerical and categorical data"
  },
  "inputs": [
    {"name": "data_set", "type": "array", "description": "Input records", "required": true},
    {"name": "analysis_type", "type": "enum", "options": ["statistical", "trend", "anomaly"], "required": true}
  ],
  "outputs": [
    {"name": "analysis_result", "type": "object", "description": "Analysis findings"}
  ],
  "steps": [
    {"id": "s1", "description": "Validate input data", "action": "check_format_and_completeness"},
    {"id": "s2", "description": "Apply analysis", "action": "execute_analysis_type"},
    {"id": "s3", "description": "Format results", "action": "structure_output"}
  ]
}
```

**Test Assertions:**
```yaml
assertions:
  - assert: 'result.status == "success" : "Execution failed"'
  - assert: 'result.test_results.total >= 10 : "Insufficient test coverage"'
  - assert: 'result.test_results.coverage >= 0.8 : "Coverage below 80%"'
  - assert: 'result.quality_metrics.quality_score >= 85 : "Quality score too low"'
  - assert: 'result.skill_file.length > 0 : "No skill file generated"'
  - assert: 'result.errors.length == 0 : "Errors detected during creation"'
  - assert: 'result.metadata.validation == "passed" : "Metadata validation failed"'
  - assert: 'result.process_completeness >= 0.95 : "Process documentation incomplete"'
```

**Expected Output:**
```json
{
  "status": "success",
  "test_results": {
    "total": 15,
    "passed": 14,
    "failed": 1,
    "skipped": 0,
    "coverage": "93.3%"
  },
  "quality_metrics": {
    "quality_score": 89,
    "documentation_completeness": 0.95,
    "test_coverage": 0.933,
    "coverage_gaps": ["error_handling_edge_case"]
  },
  "skill_file": "SKILL_EXAMPLE_ANALYZER.md",
  "validation_results": {
    "metadata": "passed",
    "context": "passed",
    "io_specification": "passed",
    "process": "passed",
    "test_suite": "passed",
    "quality": "passed"
  },
  "errors": [],
  "warnings": ["One test case needs investigation"],
  "recommendations": ["Add error handling test for empty dataset"]
}
```

---

## Testing Framework

### Running the Test Suite

```bash
# Execute all tests
skill-creator test --skill {skill_name} --verbose

# Execute specific test category
skill-creator test --skill {skill_name} --category happy_path
skill-creator test --skill {skill_name} --category edge_cases
skill-creator test --skill {skill_name} --category error_scenarios

# Generate coverage report
skill-creator test --skill {skill_name} --coverage --report html

# Run with custom assertions
skill-creator test --skill {skill_name} --assertions custom.yaml
```

### Test Report Format

```
╔════════════════════════════════════════════════════════╗
║          SKILL TEST REPORT: {skill_name}               ║
║          Generated: {timestamp}                        ║
╠════════════════════════════════════════════════════════╣
│ TEST SUMMARY                                           │
├────────────────────────────────────────────────────────┤
│ Total Tests:       25                                  │
│ Passed:            24  ✅                              │
│ Failed:            1   ❌                              │
│ Skipped:           0   ⊘                               │
│ Success Rate:      96%                                 │
├────────────────────────────────────────────────────────┤
│ COVERAGE METRICS                                       │
├────────────────────────────────────────────────────────┤
│ Code Coverage:     94.7%                               │
│ Input Coverage:    100%                                │
│ Error Path Cov:    87%                                 │
│ Branch Coverage:   91%                                 │
├────────────────────────────────────────────────────────┤
│ QUALITY SCORE                                          │
├────────────────────────────────────────────────────────┤
│ Coverage:          94.7%  (weight: 40%) = 37.88        │
│ Correctness:       96.0%  (weight: 40%) = 38.40        │
│ Documentation:     92.0%  (weight: 20%) = 18.40        │
│                    TOTAL QUALITY SCORE: 94.68/100 ✅   │
├────────────────────────────────────────────────────────┤
│ FAILED TESTS                                           │
├────────────────────────────────────────────────────────┤
│ ❌ test_edge_case_001: Empty dataset handling          │
│    Error: Expected "error", got "undefined"           │
│    File: tests/edge_cases.yaml, line 45                │
│    Recommendation: Add null-check validation          │
├────────────────────────────────────────────────────────┤
│ RECOMMENDATIONS                                        │
├────────────────────────────────────────────────────────┤
│ 1. Fix empty dataset handling test                    │
│ 2. Add integration test with external service         │
│ 3. Document timeout behavior for large datasets       │
╚════════════════════════════════════════════════════════╝
```

---

## Quick Start Example

### Create a New Skill in 5 Steps

```bash
# 1. Define skill metadata
skill-creator init \
  --name "data-validator" \
  --domain "data-quality" \
  --description "Validates data quality and generates reports"

# 2. Add context and I/O specification (interactive or YAML)
skill-creator define \
  --skill data-validator \
  --inputs-file inputs.yaml \
  --outputs-file outputs.yaml

# 3. Map process steps
skill-creator process \
  --skill data-validator \
  --from template-comprehensive

# 4. Create test suite
skill-creator test-create \
  --skill data-validator \
  --test-count 15 \
  --with-edge-cases \
  --with-error-cases

# 5. Execute tests and generate skill file
skill-creator build \
  --skill data-validator \
  --run-tests \
  --report detailed \
  --output ./skills/
```

---

## Quality Thresholds

| Metric | Threshold | Status |
|--------|-----------|--------|
| Test Coverage | ≥80% | ✅ Required |
| Assertion Pass Rate | ≥95% | ✅ Required |
| Quality Score | ≥85/100 | ✅ Required |
| Documentation | ≥90% complete | ✅ Required |
| Code Coverage | ≥85% | ⚠️ Recommended |
| Performance | <2s execution | ⚠️ Recommended |
| Error Handling | 100% paths tested | ✅ Required |

---

## Related Skills

- `agent-customization` — Extends this skill for VS Code agent customization
- `python-fact-grounded-coding` — Domain-specific knowledge for Python skills
- `project-setup-info-local` — Templates for project initialization skills

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2024-09-09 | Initial release with complete test framework |

---

## Feedback & Support

For issues, enhancements, or contributions, please reference:
- **Quality Criteria**: All metrics must meet thresholds in Quality Thresholds table
- **Test Requirements**: Minimum 10 test cases with >80% coverage
- **Documentation**: Must include all sections from this skill

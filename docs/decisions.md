# Decision log

- Variant filter: report results at minimum read depth 2 and 10, and decide which to keep
  once we can compare them (Ada wanted 5 to reduce false calls; Ben 10, about the mean depth).

- 2026-11-18: Keep minimum depth 2 for comparison with Data Carpentry and report
  sensitivity at depths 2, 5, 10 and 15. Counts change with the filter, while
  the 50,000-generation clone has more calls than the 15,000-generation clone
  at all four thresholds. This comparison describes these teaching data;
  see the report's sensitivity table and figure.

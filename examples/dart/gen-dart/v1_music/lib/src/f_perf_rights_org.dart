// Autogenerated by Frugal Compiler (1.24.1)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

library v1_music.src.f_perf_rights_org;class PerfRightsOrg {
  static const int ASCAP = 1;
  static const int BMI = 2;
  static const int SESAC = 3;
  static const int Other = 4;

  static final Set<int> VALID_VALUES = new Set.from([
    ASCAP,
    BMI,
    SESAC,
    Other,
  ]);

  static final Map<int, String> VALUES_TO_NAMES = {
    ASCAP: 'ASCAP',
    BMI: 'BMI',
    SESAC: 'SESAC',
    Other: 'Other',
  };
}

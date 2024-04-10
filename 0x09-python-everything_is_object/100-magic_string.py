def magic_string():
  magic_string.n = magic_string.n + 1 if hasattr(magic_string, 'n') else 1
  return "BestSchool, " * (magic_string.n - 1) + "BestSchool"

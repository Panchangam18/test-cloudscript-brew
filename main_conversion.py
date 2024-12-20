from CLI.transpiler.main import convert_enhanced_hcl_to_standard
from CLI.converter.main import main_convert

if __name__ == "__main__":
    main_convert(convert_enhanced_hcl_to_standard('all_tests/test2/cloud/main.cloud'))
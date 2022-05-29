# file format -> xlsx or xls
file_format = 'xlsx'

# rows to skip -> you should include headers here
# For example if 1 is empty and 2 is headers, you should write in 2
rows_to_skip = 2 

# columns in use -> You can change the main keys to have them the same
# as your excel files
columns_in_use = {
    'B': ['testsuite', 'main_parent', 'no_additional_actions'],
    'C': ['testsuite', 'sub_parent', 'optional_test_suite_present'],
    'D': ['testcase', 'sub_parent', 'no_additional_actions'],
    'E': ['importance', 'text_child', 'no_additional_actions'],
    'F': ['summary', 'text_child', 'no_additional_actions'],
    'G': ['preconditions', 'text_child', 'start_steps'],
    'H': ['actions', 'child', 'start_single_step'],
    'I': ['expectedresults', 'child', 'end_single_step']
}

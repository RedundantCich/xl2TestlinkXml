# file format -> xlsx or xls
file_format = 'xlsx'

# rows to skip -> you should include headers here
# For example if 1 is empty and 2 is headers, you should write in 3
rows_to_skip = 3

# columns in use -> You can change the main keys to have them the same
# as your excel files
columns_in_use = {
    'B': 'main_test_suite',
    'C': 'sub_test_suite',
    'D': 'test_case',
    'E': 'importance',
    'F': 'summary',
    'G': 'preconditions',
    'H': 'actions',
    'I': 'expected_results'
}

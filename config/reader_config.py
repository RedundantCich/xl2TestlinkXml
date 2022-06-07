# file format -> xlsx or xls
file_format = 'xlsx'

# rows to skip -> you should include headers here
# For example if 1 is empty and 2 is headers, you should write in 3
rows_to_skip = 3

# columns in use -> You can change the main keys to have them the same
# as your excel files
columns_in_use = {
    'B': {
        'column_role': 'main_test_suite'
        },
    'C': {
        'column_role': 'sub_test_suite'
        },
    'D': {
        'column_role': 'test_case'
        },
    'E': {
        'column_role': 'importance'
        },
    'F': {
        'column_role': 'summary'
        },
    'G': {
        'column_role': 'preconditions'
        },
    'H': {
        'column_role': 'actions'
        },
    'I': {
        'column_role': 'expected_results'
        }
}

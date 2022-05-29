# file format -> xlsx or xls
file_format = 'xlsx'

# rows to skip -> you should include headers here
# For example if 1 is empty and 2 is headers, you should write in 2
rows_to_skip = 2

# columns in use -> You can change the main keys to have them the same
# as your excel files
columns_in_use = {
    'B': {
        'column_name': 'testsuite',
        'column_role': 'main_test_suite'
        },
    'C': {
        'column_name': 'testsuite',
        'column_role': 'sub_test_suite'
        },
    'D': {
        'column_name': 'testcase',
        'column_role': 'test_case'
        },
    'E': {
        'column_name': 'importance',
        'column_role': 'in_between'
        },
    'F': {
        'column_name': 'summary',
        'column_role': 'in_between'
        },
    'G': {
        'column_name': 'preconditions',
        'column_role': 'preconditions'
        },
    'H': {
        'column_name': 'actions',
        'column_role': 'actions'
        },
    'I': {
        'column_name': 'expectedresults',
        'column_role': 'expected_results'
        }
}

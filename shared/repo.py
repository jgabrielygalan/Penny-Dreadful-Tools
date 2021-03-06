import textwrap
import traceback

from flask import request, session
from github import Github

from shared import configuration


def create_issue(content: str, author: str, location: str = 'Discord', repo_name: str = 'PennyDreadfulMTG/Penny-Dreadful-Tools', exception: None = None) -> None:
    if content is None or content == '':
        return None
    body = ''
    if '\n' in content:
        title, body = content.split('\n', 1)
        body += '\n\n'
    else:
        title = content
    body += 'Reported on {location} by {author}'.format(location=location, author=author)
    if request:
        body += textwrap.dedent("""
            --------------------------------------------------------------------------------
            Request Method: {method}
            Path: {full_path}
            Cookies: {cookies}
            Endpoint: {endpoint}
            View Args: {view_args}
            Person: {id}
            User-Agent: {user_agent}
            Referrer: {referrer}
            Request Data: {safe_data}
        """.format(method=request.method, full_path=request.full_path, cookies=request.cookies, endpoint=request.endpoint, view_args=request.view_args, id=session.get('id', 'logged_out'), user_agent=request.headers.get('User-Agent'), referrer=request.referrer, safe_data=str(safe_data(request.form))))
    if exception:
        body += '--------------------------------------------------------------------------------\n'
        body += exception.__class__.__name__ + '\n'
        stack = traceback.extract_stack()[:-3] + traceback.extract_tb(exception.__traceback__)
        pretty = traceback.format_list(stack)
        body += 'Stack Trace:\n' + ''.join(pretty) + '\n'
    print(title + '\n' + body)
    # Only check for github details at the last second to get log output even if github not configured.
    if not configuration.get('github_user') or not configuration.get('github_password'):
        return None
    g = Github(configuration.get('github_user'), configuration.get('github_password'))
    git_repo = g.get_repo(repo_name)
    issue = git_repo.create_issue(title=title, body=body)
    return issue

def safe_data(data):
    safe = {}
    for k, v in data.items():
        if 'oauth' not in k.lower() and 'api_token' not in k.lower():
            safe[k] = v
    return safe

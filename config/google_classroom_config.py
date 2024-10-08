from googleapiclient.discovery import build
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'path_to_service_account.json', scopes=['https://www.googleapis.com/auth/classroom.courses']
)
classroom_service = build('classroom', 'v1', credentials=credentials)

# Get student submissions from the quiz
submissions = classroom_service.courses().courseWork().studentSubmissions().list(courseId='your_course_id').execute()

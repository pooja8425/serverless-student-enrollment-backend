import json
import boto3
import uuid

# Initialize the DynamoDB client outside the handler to maximize container reuse performance
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentEnrollmentTable')

def lambda_handler(event, context):
    try:
        # 1. Extract and parse the stringified JSON body from API Gateway
        body = json.loads(event.get('body', '{}'))
        
        student_name = body.get('student_name')
        course = body.get('course')
        email = body.get('email')
        
        # Data Validation Check
        if not student_name or not course or not email:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Missing required fields: student_name, course, or email'})
            }
            
        # 2. Programmatically auto-generate a unique 8-character ID for the student
        unique_student_id = str(uuid.uuid4())[:8]
        
        # 3. Insert the parsed record directly into the NoSQL DynamoDB Table
        table.put_item(
            Item={
                'student_id': unique_student_id,
                'student_name': student_name,
                'course': course,
                'email': email
            }
        )
        
        # 4. Issue a successful creation response to the calling application with CORS enabled
        return {
            'statusCode': 201,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST'
            },
            'body': json.dumps({
                'message': 'Student enrolled successfully!',
                'student_id': unique_student_id
            })
        }
        
    except Exception as e:
        print(f"Exception logging: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Internal Server Error'})
        }

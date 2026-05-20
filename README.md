# Serverless Student Enrollment Backend API

## Project Overview
Traditional dynamic web applications rely on fixed servers running 24/7 just to handle data entry workflows (like student registrations, inquiry forms, or customer sign-ups). This architecture results in severe cost inefficiencies during traffic dead zones and exposes the platform to crashes during unexpected spikes. 

This project delivers a **100% Serverless Backend REST API** that completely decouples infrastructure from application code. The application handles user requests, automatically scales dynamically to incoming spikes, and runs entirely within the AWS Free Tier with $0 baseline overhead.

## Architecture Diagram

<img width="496" height="115" alt="image" src="https://github.com/user-attachments/assets/16fdeea3-17ff-469b-abe1-23aac4785f9c" />



## AWS Services & Tech Stack Used
* **Amazon API Gateway (HTTP API):** Acts as the secure, high-throughput public-facing front door, handling routing and CORS validation.
* **AWS Lambda:** Exposes an asynchronous serverless execution workspace running Python to validate, process, and map application workloads.
* **Amazon DynamoDB:** A high-speed, fully managed NoSQL database acting as the storage layer for structured records.
* **AWS IAM:** Restricts cross-service communication access through fine-grained execution policies enforcing least privilege.

## Key Features
* **Auto-Scaling Infrastructure:** Because the system is entirely serverless, it scales from zero requests up to thousands of requests per second smoothly without any infrastructure intervention.
* **Cross-Origin Resource Sharing (CORS):** Fully configured CORS mapping within API Gateway allows external web forms and applications to query the backend securely.
* **Dynamic Record Tagging:** Built micro-logic using Python's `uuid` library to automatically create distinct short-form IDs for incoming payloads inside the partition key space.

## Deployment Configuration
1. **Database Setup:** Initialize an Amazon DynamoDB table named `StudentEnrollmentTable` using a String Partition Key named `student_id`.
2. **Access Control:** Map an IAM execution role featuring strict `dynamodb:PutItem` execution permissions for security scoping.
3. **Lambda Setup:** Deploy the microservice script inside `lambda_function.py`, attaching the generated IAM security role.
4. **API Integration:** Provision an API Gateway instance running a `POST /enroll` route directing traffic workflows straight into the Lambda target.

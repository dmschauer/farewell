from farewell import on_exit
import boto3
import os

# SNS setup
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:script-alerts"
SCRIPT_NAME = "data_processing_job"

# Create SNS client
sns_client = boto3.client('sns', region_name='us-east-1')

def send_success_notification():
    """Called when script completes successfully"""
    message = f"✅ {SCRIPT_NAME} completed successfully!"
    
    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f"[SUCCESS] {SCRIPT_NAME}",
        Message=message
    )
    print("Success notification sent!")

def send_error_notification(error_info):
    """Called when script fails with an exception"""
    message = f"""❌ {SCRIPT_NAME} failed!

Error Type: {error_info['type']}
Error Message: {error_info['message']}

Full Traceback:
{error_info['traceback']}"""
    
    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f"[ERROR] {SCRIPT_NAME}",
        Message=message
    )
    print("Error notification sent!")

# Register the notification handlers - this will validate the functions!
on_exit(send_success_notification, send_error_notification)

# ============================================================================
# YOUR ACTUAL SCRIPT LOGIC BELOW - completely unchanged!
# ============================================================================

print("Starting data processing...")

# Simulate some work
data = [1, 2, 3, 4, 5]
result = sum(data) * 2
print(f"Processed {len(data)} items, result: {result}")

# More work
for i in range(3):
    print(f"Processing batch {i+1}...")

# Uncomment ONE of these to test error notifications:
# raise ValueError("Database connection failed!")
# raise FileNotFoundError("Input file missing!")
# result = 10 / 0  # ZeroDivisionError

print("Data processing completed!")

# That's it! When the script ends (successfully or with error),
# the appropriate SNS notification will be sent automatically.
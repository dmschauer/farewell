# Farewell

<div style="display: flex; align-items: center; justify-content: center;">
    <a href="https://dmschauer.github.io/farewell" style="margin-right: 20px;">
        <img src="img/farewell_icon_white_border.png" style="width: 100px;" alt="Farewell logo"/>
    </a>
    <em style="font-size: 1.1em;">
        Simple, unobtrusive script exit notifications.
    </em>
</div>

`Farewell` is a basic utility package. It calls a custom function on succesful script exits and another custom function in case of any error. It is similar to wrapping everything into a `try/except` block, but without the need to change your script logic or indent your code.

The intended use case is sending notifications in case of succesful/failed job runs.

## Installation

```python
pip install farewell
```

## Quick examples

### Basic usage

```python
from farewell import on_exit

def on_success():
    print("✅ Everything worked!")

def on_error(error):
    print(f"❌ Failed: {error['type']} - {error['message']}")

on_exit(success_func=on_success,
        error_func=on_error)

# You actual script logic below - completely unchanged!
print("Script running...")

# Uncomment to test error:
# raise ValueError("Test error!")

print("Script finished!")
```

### Usage with a main()

```python
from farewell import on_exit

def setup_notifications() :
    def success_notification():
        print("✅ Everything worked!")
    
    def error_notification(error):
        print(f"❌ Failed: {error['type']} - {error['message']}")

    on_exit(success_notification, error_notification)

def main():
    print("Script running...")
    
    # Uncomment to test error:
    # raise ValueError("Test error!")
    
    print("Script finished!")

if __name__ == "__main__":
    setup_notifications() # could also be called inside main()
    main()
```

### Example with AWS SNS notifications

Also checkout `./examples/sns.py` for a more complete example.

```python
from farewell import on_exit
import boto3

sns = boto3.client('sns')

def notify_success():
    sns.publish(TopicArn="...", Message="✅ Everything worked!")

def notify_error(err):
    sns.publish(TopicArn="...", Message=f"❌ Failed: {err['type']} - {err['message']}")

on_exit(succes_func=notify_success,
        error_func=notify_error)

# You actual script logic below - completely unchanged!
```

# Timothy Vaculik
# sending messages with functions
# I think is is difficulty of 6/10




def display_message(messages):
    """Display all messages."""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Send messages and move them to sent_messages."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


messages = ["Hey, how are ya?", "what's up?", "how's it going?"]
sent_messages = []


send_messages(messages, sent_messages)
display_message(sent_messages)

print("\nOriginal messages list:")
print(messages)
print("\nSent messages list:")
print(sent_messages)
from collections import defaultdict


def best_sender(messages, sender):
    dict_senders = defaultdict(int)

    for i in range(len(sender)):
        dict_senders[sender[i]] += len(messages[i].split())

    return sorted(
        dict_senders.items(), key=lambda sender: (sender[1], sender[0]), reverse=True
    )[0][0]


messages = [
    "How is Stepik for everyone",

    "How is Stepik for everyone"
]
senders = ["Bob", "Charlie"]

print(best_sender(messages, senders))

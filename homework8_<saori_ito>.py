def make_sandwich (*ingredients):
    """Summarize the sandwich we are about to make."""
    print("\nSandwich order:")
    for ingredient in ingredients:
        print (f"-{ingredient}")
make_sandwich ('ham', 'cheese', 'tomato', 'lettuce', 'oil', 'vinegar')
make_sandwich ('ham', 'cheese', 'lettuce', 'mayo', 'mustard')
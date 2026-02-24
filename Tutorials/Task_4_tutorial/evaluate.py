def get_F_score(predictions, ground_truths):
    
    num_true = sum((pred["prediction"] == 1 and int(gt) == 1) for pred, gt in zip(predictions, ground_truths))
    num_false_negative = sum((pred["prediction"] == 0 and int(gt) == 1) for pred, gt in zip(predictions, ground_truths))
    num_false_positive = sum((pred["prediction"] == 1 and int(gt) == 0) for pred, gt in zip(predictions, ground_truths))

    factor = 0.5
    precision = num_true / (num_true + num_false_positive) if (num_true + num_false_positive) else 0
    recall = num_true / (num_true + num_false_negative) if (num_true + num_false_negative) else 0
    
    
    F = (1 + factor**2) * (precision * recall) / (factor**2 * precision + recall) if (precision + recall) else 0
    
    
    acc = (num_true + sum((pred["prediction"] == 0 and int(gt) == 0) for pred, gt in zip(predictions, ground_truths))) / len(predictions)
    
    return F, acc
    
    
    
def get_score_from_df(df):
    num_true = sum(df["correctness"] == "True positive")
    num_false_negative = sum(df["correctness"] == "False negative")
    num_false_positive = sum(df["correctness"] == "False positive")

    factor = 0.5
    precision = num_true / (num_true + num_false_positive) if (num_true + num_false_positive) else 0
    recall = num_true / (num_true + num_false_negative) if (num_true + num_false_negative) else 0
    F = (1 + factor**2) * (precision * recall) / (factor**2 * precision + recall) if (precision + recall) else 0
    acc = (len(df) - num_false_negative - num_false_positive) / len(df)
    return F, acc
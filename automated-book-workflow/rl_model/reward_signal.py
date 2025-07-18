# computing reward from original, spun, reviewed text using lexical approach

def compute_reward(original, spun, reviewed, feedback_score):
    #reward calculation logic
    lexical_diversity = len(set(spun.split())) / len(spun.split())
    
    semantic_preservation = 1.0  # Stubbed metric for now
    return (0.4 * lexical_diversity) + (0.4 * semantic_preservation) + (0.2 * feedback_score)
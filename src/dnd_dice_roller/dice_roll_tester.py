from dice_roller import die_roll
from dice_roller import dice_roll_dist
from scipy.stats import kruskal
from scipy.stats import ttest_ind as t_test

def perfect_uniform_die(die_size:int=20, num_each:int=1000):
    distribution = []
    for i in range(1,die_size+1):
        distribution.extend([i] * num_each)
    return distribution

def expected_diff(die_size:int=20):
    abs_diffs = []
    for i in range(1,die_size+1):
        for j in range(1,die_size+1):
            diff = i-j
            abs_diffs.append(abs(diff))
    expected = sum(abs_diffs)/len(abs_diffs)
    return expected, abs_diffs

def streak_test(rolls:list,die_size:int=None):
    if die_size is None:
        die_size = max(rolls)
    
    exp_diff,exp_list = expected_diff(die_size)
    
    diffs = []
    abs_diffs = []
    for i in range(1,len(rolls)):
        seq_diff = rolls[i] - rolls[i-1]
        diffs.append(seq_diff)
        abs_diffs.append(abs(seq_diff))
    
    mean_diff = sum(diffs)/len(diffs)
    mean_abs_diff = sum(abs_diffs)/len(abs_diffs)
    
    t_test_result = t_test(abs_diffs,exp_list)
    p_val = t_test_result.pvalue
    return p_val,mean_abs_diff,exp_diff

def test_dice(die_size:int=20, rolls:int=10000, alpha:float=0.05, silent:bool=False):
    exp_mean = die_size/2 + 0.5
    mean,counts,roll_dist = dice_roll_dist(die_size,rolls)
    
    kruskal_result = kruskal(roll_dist,perfect_uniform_die(die_size,round(rolls/die_size)))
    k_p_val = kruskal_result.pvalue

    t_p_val,mean_abs_diff,exp_diff = streak_test(roll_dist,die_size)
    
    problems = []    
    
    if k_p_val < alpha:
        fair_dist = False
        problems.append('a skewed distribution')
    else:
        fair_dist = True
        
    if t_p_val < alpha:
        fair_streak = False
        problems.append('streaking')
    else:
        fair_streak = True
    
    if fair_dist and fair_streak:
        is_fair = "This die is fair."
    else:
        is_fair = f'This die is NOT fair, due to {" and ".join(problems)}.'
    
    if not silent:
        print(f'd{die_size} Test:')
        for i in counts:
            print(f'\t{i}: {counts[i]}')
        print(f'\n{is_fair}')
        print(f'\nAverage Roll: {round(mean,2)} (Expected: {exp_mean})')
        print(f'Distribution p-Value: {round(k_p_val,4)}')
        print(f'\nMean Sequential Difference: {round(mean_abs_diff,3)} (Expected: {round(exp_diff,3)})')
        print(f'Streak p-value: {round(t_p_val,4)}')
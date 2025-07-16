# Program for mean, medium and mode
import statistics
def mean_medium_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)

#print(mean_medium_mode([3,4,6,2,34,76]))
a,b,c= mean_medium_mode([3,4,6,2,34,76])
print(f"Mean is {a}\nMeidum is {b}\nMode is {c}")
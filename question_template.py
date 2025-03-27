# Template for writing solutions for practical lists of "Análise e Técnicas
# de Algoritmos".

def solution():
    # [TODO] Write the question solution here...
    pass


def run_tests():
    num_tests = int(input())
    results = [0 for _ in range(num_tests)]

    for i in range(num_tests):
        # [WARN] Remember to reset variables used for storing results!
        # [TODO] Do some input parsing here...
        # [TIP]  Quick way to parse a list of integers from input:
        # parsed_vals = map(int, input().split())
        
        results[i] = solution()

    for result in results:
        print(result)


if __name__ == "__main__":
    # [TODO] Declare global variables here, if any...
    run_tests()

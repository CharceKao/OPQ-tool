def OPQ():
    
    guesses_a_counts = {}
    guesses = ["000", "100", "010", "001"]

    print("請依序輸入以下猜測組合得到的 A 的數量 (輸入後按 Enter):")

    for guess in guesses:
        while True:
            try:
                a_count = int(input(f"猜測組合 {guess} 的 A 的數量 (0 或 1): "))
                if 0 <= a_count <= 1:
                    guesses_a_counts[guess] = a_count
                    break
                else:
                    print("輸入錯誤，請輸入 0 或 1。")
            except ValueError:
                print("輸入錯誤，請輸入一個整數。")

    possible_distributions = []

    for c1 in range(5):  
        for c2 in range(5 - c1):  
            c3 = 4 - c1 - c2

            if 0 <= c3 <= 4:
                actual_distribution = (c1, c2, c3)
                all_guesses_match = True

                for guess, a_count in guesses_a_counts.items():
                    match_count = 0
                    guess_c1 = int(guess[0])
                    guess_c2 = int(guess[1])
                    guess_c3 = int(guess[2])

                    if guess_c1 == actual_distribution[0]:
                        match_count += 1
                    if guess_c2 == actual_distribution[1]:
                        match_count += 1
                    if guess_c3 == actual_distribution[2]:
                        match_count += 1

                    if match_count != a_count:
                        all_guesses_match = False
                        break

                if all_guesses_match:
                    possible_distributions.append(actual_distribution)

    return possible_distributions

if __name__ == "__main__":
    results = OPQ()

    if results:
        print("\n答案:")
        for distribution in results:
            print(distribution)
    else:
        print("\n沒有答案")

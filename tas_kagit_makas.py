import random

# T>M, M>K, K>T
hand_list = {
    "T": "Taş",
    "K": "Kağıt",
    "M": "Makas"
}
def start_game():
    hand = input("Seçiminizi yapınız Taş(T) mı Kağıt(K) mı Makas(M) mı??? ").upper()
    bot_hand = random.choice(list(hand_list.keys()))

    message = f'Seçiminiz: {hand_list[hand]}, bilgisayarın seçimi {hand_list[bot_hand]}'

    if hand == bot_hand:
        message = f"BERABERLİK! {message}"
    elif is_win(hand, bot_hand):
        message = f"KAZANDINIZ! {message}"
    else:
        message = f"KAYBETTİNİZ! {message}"

    return message #print işlevinde

def is_win(player, bot):
    # T>M, M>K, K>T
    return (player == 'T' and bot == 'M') or (player == 'M' and bot == 'K') or (player == 'K' and bot == 'T')



finish = start_game()
print(finish)

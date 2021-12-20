from collections import defaultdict

def solution(genres, plays):
    music_dict = defaultdict(list)
    music_sum_dict = defaultdict(int)
    music_idx = 0

    # genre별 play 수 합산
    for genre, play in zip(genres, plays):
        music_dict[genre].append((music_idx, play))
        music_sum_dict[genre] += play
        music_idx += 1
    # play 수별 정렬
    sorted_sum_dict = sorted(music_sum_dict.items(), key=lambda item:item[1], reverse=True)

    # play 수별 idx 정렬
    answer = []
    for genre, _ in sorted_sum_dict:
        sorted_music_list = sorted(music_dict[genre], key=lambda item:item[1], reverse=True)
        answer += [idx for idx, _ in sorted_music_list][:2]

    return answer
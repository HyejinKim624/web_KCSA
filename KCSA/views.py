from django.shortcuts import render
from .models import VoiceFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return render(request, 'KCSA/home.html', {})

def tracklist(request):    
    # 페이지 받아오기
    page = request.GET.get('page', '1')

    # 트랙리스트 조회
    track = VoiceFile.objects.all()

    # 페이징처리
    paginator = Paginator(track, 6)
    try:                                
        track = paginator.page(page)
    except PageNotAnInteger:        # 페이지 번호가 없으면
        track = paginator.page(1)   # 첫번째 페이지를 보여줌
    except EmptyPage:                               # 페이지가 비어있으면(페이지 번호 초과시)
        page = paginator.page(paginator.num_pages)  # 마지막 페이지를 보여줌

    # 해당 페이지 index
    index = track.number

    # 마지막 페이지
    max_index = len(paginator.page_range)

    # 하단에 보여줄 페이지 범위 크기
    page_size = 5

    # 해당 페이지에서 앞으로 두칸 --> page_size보다 작으면 1
    start_index = index - page_size if index > page_size else 1

    # 해당 페이지에서 뒤로 두칸
    if index + page_size == max_index:  # 총 페이지가 3칸 이하면
        end_index = max_index
    else:   # 현재 페이지+page_size가 max보다 크면 max로 설정
        end_index = index + page_size if index <= max_index else max_index
    
    # 리스트는 0부터 시작
    page_range = list(paginator.page_range[start_index-1 : end_index])
    
    return render(request, 'KCSA/tracklist.html', {'track':track, 'page_range':page_range, 'max_index':max_index, 'page_size':page_size})
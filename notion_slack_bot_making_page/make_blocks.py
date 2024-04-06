from blocks.text_blocks import *
from blocks.etc_blocks import *

def make_blocks():
    parts = ('기획', '관객 서버', '매니저 서버', '클라이언트', '디자인')
    colors = ('orange_background', 'yellow_background', 'green_background', 'blue_background', 'purple_background')
    # parts_block을 구성하는 부분 수정
    parts_block = []
    for part, color in zip(parts, colors):
        parts_block.append(Heading2Block(part, color=color).to_dict)  # Heading2Block 추가
        # 예정, 현황에 대한 Heading3Block들 추가
        for content in ('예정', '현황'):
            parts_block.append(Heading3Block(content).to_dict)
            
    original_parts_block = [
        Heading2Block(part, color=color).to_dict
        for part, color in zip(parts, colors)    
    ]
    
    result = [
            Heading1Block('파트별 진행 상황 공유').to_dict
        ] + parts_block + [
            Heading1Block('회고').to_dict
        ] + [
            Heading1Block('다음 스프린트 목표').to_dict
        ] + original_parts_block 
    return result
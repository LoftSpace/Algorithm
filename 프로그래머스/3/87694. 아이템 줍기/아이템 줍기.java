class Solution {

    int itemX, itemY;
    int[][] rectangle;
    int len;

    int[] dx = {1, -1, 0, 0};  // 우, 좌, 상, 하
    int[] dy = {0, 0, 1, -1};
    int minDistance = Integer.MAX_VALUE;

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        this.itemX = itemX * 2;
        this.itemY = itemY * 2;
        this.rectangle = rectangle;
        this.len = rectangle.length;

        // 좌표를 2배 확장하여 경계선을 정확히 구분
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < 4; j++) {
                this.rectangle[i][j] *= 2;
            }
        }

        int startX = characterX * 2;
        int startY = characterY * 2;

        // 시작 좌표가 여러 사각형의 경계에 걸쳐 있을 수 있으므로 가능한 모든 사각형 index에서 추적 시작
        for (int i = 0; i < len; i++) {
            if (isEdge(startX, startY, i)) {
                trace(startX, startY, i, 0, startX, startY);
            }
        }

        // 결과를 다시 2로 나눠 원래 거리로 환산
        return minDistance / 2;
    }

    public void trace(int x, int y, int index, int distance, int visitedX, int visitedY) {
        // 목적지 도달 시 최소 거리 갱신
        if (x == itemX && y == itemY) {
            minDistance = Math.min(minDistance, distance);
            return;
        }

        // 현재 좌표가 포함된 사각형 index 찾기
        while (!isEdge(x, y, index)) index = (index + 1) % len;

        // 4방향으로 이동
        Outter : for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];

            // 직전 위치로는 되돌아가지 않음
            if (nx == visitedX && ny == visitedY) continue;

            // 이동 좌표가 현재 사각형의 경계 위인 경우
            if (isEdge(nx, ny, index)) {
                int next = index;

                // 이동하려는 좌표가 다른 사각형 내부에 속하는지 확인
                for (int j = 0; j < len - 1; j++) {
                    next = (next + 1) % len;
                    if (isInside(nx, ny, next)) continue Outter;  // 내부면 외곽 아님
                }

                // 다음 좌표로 이동
                trace(nx, ny, (index + 1) % len, distance + 1, x, y);
            }
        }
    }

    // 현재 좌표가 사각형의 테두리 위에 있는지 판별
    public boolean isEdge(int x, int y, int index) {
        int[] rect = rectangle[index];
        if (x < rect[0] || x > rect[2] || y < rect[1] || y > rect[3]) return false;
        return x == rect[0] || x == rect[2] || y == rect[1] || y == rect[3];
    }

    // 현재 좌표가 사각형 내부에 있는지 판별
    public boolean isInside(int x, int y, int index) {
        int[] rect = rectangle[index];
        return rect[0] < x && x < rect[2] && rect[1] < y && y < rect[3];
    }
}

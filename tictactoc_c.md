'''
#include<stdio.h>
char player = 'X', computer='O';
char b[3][3]={	 {'1','2','3'},
				 {'4','5','6'},
				 {'7','8','9'}
			   };
void board() {
	
	printf("%c|%c|%c\n", b[0][0],b[0][1],b[0][2]);
	printf("-+-+-\n");
	printf("%c|%c|%c\n", b[1][0],b[1][1],b[1][2]);
	printf("-+-+-\n");
	printf("%c|%c|%c\n", b[2][0],b[2][1],b[2][2] );
}
void player_pos() {
	int pos;
	printf("Player : 위치를 정해주세요: ");
	scanf("%d", &pos);
	if (pos == 1) {
		b[0][0] = player;
	}
}
void computer_pos() {
	int pos;
	printf("Computer : 위치를 정해주세요: ");
	scanf("%d", &pos);
	if (pos == 2) {
		b[0][1] = computer;
	}
}
int main() {		
		board();
		player_pos();
		board();
		computer_pos();
		board();
	return 0;
}
'''

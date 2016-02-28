# NemoSemo-Reasoning-Game
#GraphMaking.py
#class GraphMaking
 ##MakeGraph(self, RandomGraph = True, UserTable = True)
-	객채의 랜덤 그래프와 유저 테이블을 생성한다.
-	속성 값은 기본적으로 MakeGraph(self, True, True)로 되어있다. (입력하지 않으면 자동적으로 MakeGraph(self, True, True) )
-	RandomGraph 값을 False로 할 시 랜덤 그래프를 그리지 않는다.
-	UserTable 값을 False로 할 시 유저 테이블을 만들지 않는다.
 ##RemoveGraph(self, RandomGraph = True,UserGraph = True)
-	객체의 랜덤 그래프와 유저 그래프를 랜텀 테이블, 유저 테이블로 변환한다. 
-	속성 값은 기본적으로 RemoveGraph(self, True,True)로 되어있다. (입력하지 않으면 자동적으로 RemoveGraph(self, True,True)
-	RandomGraph 값을 False로 할 시 랜덤 테이블로 변환하지 않는다.
-	UserGraph 값을 False로 할 시 유저 테이블로 변환하지 않는다.
#Debug.py
 ※	디버그모드를 사용하려면 디버그모드를 사용할 class에 디버그 class를 상속시켜야 한다.
#Class DebugMatrix
 ##show(self, RandomGraph = True, UserGraph = True)
-	사용하기 위해 DebugMatrix를 MatrixMaking에 상속시켜야 한다. ( GraphMaking(DebugMatrix) )
-	객체의 랜덤 그래프와 유저 그래프를 출력한다. 
-	객체의 랜덤 그래프 혹은 유저 그래프가 존재하지 않을시 "NOT FOUND MATRIX"를 출력한다.
-	속성 값은 기본적으로 show(self, True,True)로 되어있다. (입력하지 않으면 자동적으로 show(self, True,True)
-	RandomGraph의 값을 False로 할 시 랜덤 그래프를 출력하지 않는다.
-	UserGraph의 값을 False로 할 시 유저 그래프를 출력하지 않는다.
#Gameplay.py 
-설명 작성중...
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'dog' and NAME like '%el%'
ORDER BY NAME
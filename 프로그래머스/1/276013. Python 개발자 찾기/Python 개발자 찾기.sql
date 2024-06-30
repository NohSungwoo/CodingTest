-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME 
FROM DEVELOPER_INFOS
WHERE SKILL_1 Like 'python' or SKILL_2 Like 'python' or SKILL_3 Like 'python'
ORDER BY ID;
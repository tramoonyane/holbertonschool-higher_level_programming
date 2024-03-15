-- SQL query to list all shows with at least one genre linked in the hbtn_0d_tvshows database

-- Query to list all shows with at least one genre linked and sort by title and genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

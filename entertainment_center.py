import media
import fresh_tomatoes

hacksaw = media.Movie("Hacksaw Ridge",
                      ("The true story of Pfc. Desmond T. Doss"
                       " (Andrew Garfield), who won the Congressional"
                       " Medal of Honor despite refusing to bear arms during WWII on religious grounds."),
                      "https://upload.wikimedia.org/wikipedia/pt/thumb/a/a0/Hacksaw_Ridge.png/250px-Hacksaw_Ridge.png",
                      "https://www.youtube.com/watch?v=s2-1hz1juBI")

war_room = media.Movie("War Room",
                       ("With great jobs, a beautiful daughter (Alena Pitts) "
                        "and a dream house, the Jordans seem to have it all. "),
                       "https://images-na.ssl-images-amazon.com/images/I/51d5Ql7hrHL._SX331_BO1,204,203,200_.jpg",
                       "https://www.youtube.com/watch?v=2DbRwcrhiLA")

god_is_not_dead = media.Movie("God is not dead",
                              ("The Rev. Dave Hill faces an unexpected setback "
                               "when his beloved church burns down -- "
                               "prompting the officials at the adjoining university "
                               "to try and kick his congregation off campus."),
                              "https://upload.wikimedia.org/wikipedia/en/c/cf/God%27s_Not_Dead.jpg",
                              "https://www.youtube.com/watch?v=wIKExeMVksk")

pursuit = media.Movie("The Pursuit of Happyness",
                      ("Life is a struggle for single father Chris Gardner (Will Smith). "
                       "Evicted from their apartment, he and his young son (Jaden Christopher"
                       " Syre Smith) find themselves alone with no place to go."),
                      "https://upload.wikimedia.org/wikipedia/pt/thumb/1/1e/The_Pursuit_of_Happyness.jpg/200px-The_Pursuit_of_Happyness.jpg",
                      "https://www.youtube.com/watch?v=89Kq8SDyvfg")


movies = [hacksaw, war_room, god_is_not_dead, pursuit]
fresh_tomatoes.open_movies_page(movies)

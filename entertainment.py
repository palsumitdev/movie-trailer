# Thes modules are the requirements to generate a html page
import media
import fresh_tomatoes

# This is for creating the instance of movie
toy_story = media.Movie("Toy Story", """A story of a boy
                        and his toys that come to life""",
                       "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # Noqa
                         "https://www.youtube.com/watch?v=Pl9JS8-gnWQ")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # Noqa
                     "https://www.youtube.com/watch?v=WbMD53XPJWA")

school_of_rock = media.Movie("School of Rock", "Using Rock music to learn",
                             "https://cdn.shopify.com/s/files/1/1416/8662/products/School_of_Rock_2003_original_film_art_2000x.jpg?v=1551894410",  # Noqa
                             "https://www.youtube.com/watch?v=4AeUHwkIJzU")

ratatouile = media.Movie("Ratatouille", "A rat is a chef in paris",
                         "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # Noqa
                         "https://www.youtube.com/watch?v=nTTxc1Vf2pQ")

midnight_in_paris = media.Movie("Midnight in Paris", """Going
                                 back in time to meet authors""",
                                "https://mir-s3-cdn-cf.behance.net/project_modules/disp/d2df8d39239867.5606ad25121f6.jpg",  # Noqa
                                "https://www.youtube.com/watch?v=dtiklALGz20")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # Noqa
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

avenger_infinity = media.Movie("Avenger Infinity War", """A fight
                              between the avengers and the thanos""",
                             "https://render.fineartamerica.com/images/rendered/default/poster/8/10/break/images/artworkimages/medium/1/4-avengers-infinity-war-geek-n-rock.jpg",  # Noqa
                             "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

thor_rangarok = media.Movie("Thor Rangarok", """Fight
                           between sister and brother""",
                          "https://www.filmibeat.com/ph-big/2017/04/thor-ragnarok_149249270490.jpg",  # Noqa
                          "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

avenger_end = media.Movie("Avenger End Game", """Final battle
                          between avengers and thanos""",
                          "https://wallpapercave.com/wp/wp3850245.jpg",
                          "https://www.youtube.com/watch?v=TcMBFSGVi1c")

captain_marvel = media.Movie("Captain Marvel", """The extreme
                              power of captain marvel""",
                             "https://wallpapercave.com/wp/wp3891882.jpg",
                             "https://www.youtube.com/watch?v=Z1BCujX3pw8")

doctor_strange = media.Movie(" Docor Strange", """Doctor know the
                              another part of the universe""",
                             "https://wallpapercave.com/wp/wp2028638.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")
movies = [toy_story, avatar, school_of_rock,
          ratatouile, midnight_in_paris, hunger_games,
          avenger_infinity, thor_rangarok, avenger_end,
          captain_marvel, doctor_strange]
# this function is to generate a dynamically generated html page
fresh_tomatoes.open_movies_page(movies)

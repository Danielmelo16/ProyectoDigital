# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

URL = ["http://rosettacode.org/wiki/100_doors", "http://rosettacode.org/wiki/99_Bottles_of_Beer", "http://rosettacode.org/wiki/Abundant,_deficient_and_perfect_number_classifications",
        "http://rosettacode.org/wiki/Accumulator_factory", "http://rosettacode.org/wiki/Ackermann_function", "http://rosettacode.org/wiki/Add_a_variable_to_a_class_instance_at_runtime",
        "http://rosettacode.org/wiki/Amicable_pairs", "http://rosettacode.org/wiki/Angle_difference_between_two_bearings", "http://rosettacode.org/wiki/Apply_a_callback_to_an_array",
        "http://rosettacode.org/wiki/Arithmetic/Integer", "http://rosettacode.org/wiki/Associative_array/Creation", "http://rosettacode.org/wiki/Associative_array/Iteration",
        "http://rosettacode.org/wiki/Averages/Median", "http://rosettacode.org/wiki/Averages/Root_mean_square", "http://rosettacode.org/wiki/Balanced_ternary",
        "http://rosettacode.org/wiki/Bernoulli_numbers", "http://rosettacode.org/wiki/Binary_digits", "http://rosettacode.org/wiki/Bitmap/B%C3%A9zier_curves/Quadratic",
        "http://rosettacode.org/wiki/Brownian_tree", "http://rosettacode.org/wiki/Canny_edge_detector", "http://rosettacode.org/wiki/Cartesian_product_of_two_or_more_lists",
        "http://rosettacode.org/wiki/Catamorphism", "http://rosettacode.org/wiki/Checkpoint_synchronization", "http://rosettacode.org/wiki/Classes",
        "http://rosettacode.org/wiki/Closures/Value_capture", "http://rosettacode.org/wiki/Collections", "http://rosettacode.org/wiki/Colour_pinstripe/Printer",
        "http://rosettacode.org/wiki/Compare_a_list_of_strings", "http://rosettacode.org/wiki/Conjugate_transpose", "http://rosettacode.org/wiki/Convert_decimal_number_to_rational",
        "http://rosettacode.org/wiki/Count_the_coins", "http://rosettacode.org/wiki/CRC-32", "http://rosettacode.org/wiki/Deconvolution/2D%2B", "http://rosettacode.org/wiki/Dinesman%27s_multiple-dwelling_problem",
        "http://rosettacode.org/wiki/Draw_a_clock", "http://rosettacode.org/wiki/Elementary_cellular_automaton", "http://rosettacode.org/wiki/Empty_program",
        "http://rosettacode.org/wiki/Enumerations", "http://rosettacode.org/wiki/Euler_method", "http://rosettacode.org/wiki/Exceptions/Catch_an_exception_thrown_in_a_nested_call",
        "http://rosettacode.org/wiki/Execute_SNUSP", "http://rosettacode.org/wiki/Extend_your_language", "http://rosettacode.org/wiki/Factors_of_a_Mersenne_number",
        "http://rosettacode.org/wiki/Factors_of_an_integer", "http://rosettacode.org/wiki/First_class_environments", "http://rosettacode.org/wiki/Floyd-Warshall_algorithm",
        "http://rosettacode.org/wiki/Generic_swap", "http://rosettacode.org/wiki/Grayscale_image", "http://rosettacode.org/wiki/Guess_the_number/With_feedback_(player)",
        "http://rosettacode.org/wiki/Heronian_triangles", "http://rosettacode.org/wiki/Hofstadter-Conway_$10,000_sequence", "http://rosettacode.org/wiki/Holidays_related_to_Easter",
        "http://rosettacode.org/wiki/Honeycombs", "http://rosettacode.org/wiki/Hough_transform", "http://rosettacode.org/wiki/Infinity", "http://rosettacode.org/wiki/Inverted_syntax",
        "http://rosettacode.org/wiki/Knapsack_problem/Bounded", "http://rosettacode.org/wiki/Knight%27s_tour", "http://rosettacode.org/wiki/Knuth%27s_algorithm_S",
        "http://rosettacode.org/wiki/Kronecker_product_based_fractals", "http://rosettacode.org/wiki/Leap_year", "http://rosettacode.org/wiki/Long_multiplication",
        "http://rosettacode.org/wiki/Longest_common_subsequence", "http://rosettacode.org/wiki/Ludic_numbers", "http://rosettacode.org/wiki/Magic_squares_of_odd_order",
        "http://rosettacode.org/wiki/Magic_squares_of_singly_even_order", "http://rosettacode.org/wiki/Maximum_triangle_path_sum", "http://rosettacode.org/wiki/MD4",
        "http://rosettacode.org/wiki/Modular_inverse", "http://rosettacode.org/wiki/Monty_Hall_problem", "http://rosettacode.org/wiki/Multiple_distinct_objects",
        "http://rosettacode.org/wiki/Numeric_error_propagation", "http://rosettacode.org/wiki/OLE_Automation", "http://rosettacode.org/wiki/One_of_n_lines_in_a_file",
        "http://rosettacode.org/wiki/Operator_precedence","http://rosettacode.org/wiki/Ordered_Partitions", "http://rosettacode.org/wiki/Paraffins", "http://rosettacode.org/wiki/Permutations/Rank_of_a_permutation",
        "http://rosettacode.org/wiki/Pig_the_dice_game", "http://rosettacode.org/wiki/Pig_the_dice_game/Player", "http://rosettacode.org/wiki/Pinstripe/Printer",
        "http://rosettacode.org/wiki/Play_recorded_sounds", "http://rosettacode.org/wiki/Polyspiral", "http://rosettacode.org/wiki/Primes_-_allocate_descendants_to_their_ancestors"
        "http://rosettacode.org/wiki/Probabilistic_choice", "http://rosettacode.org/wiki/Quickselect_algorithm", "http://rosettacode.org/wiki/Quine",
        "http://rosettacode.org/wiki/Range_expansion", "http://rosettacode.org/wiki/Ranking_methods", "http://rosettacode.org/wiki/RCRPG", "http://rosettacode.org/wiki/Rendezvous",
        "http://rosettacode.org/wiki/Return_multiple_values", "http://rosettacode.org/wiki/Roots_of_a_function", "http://rosettacode.org/wiki/Set_puzzle",
        "http://rosettacode.org/wiki/Sierpinski_carpet", "http://rosettacode.org/wiki/Sierpinski_pentagon", "http://rosettacode.org/wiki/Sierpinski_triangle",
        "http://rosettacode.org/wiki/Simple_windowed_application", "http://rosettacode.org/wiki/Simulate_input/Keyboard", "http://rosettacode.org/wiki/Sleep",
        "http://rosettacode.org/wiki/Sokoban", "http://rosettacode.org/wiki/Sort_disjoint_sublist", "http://rosettacode.org/wiki/Sorting_algorithms/Comb_sort",
        "http://rosettacode.org/wiki/Sorting_algorithms/Shell_sort", "http://rosettacode.org/wiki/Statistics/Basic", "http://rosettacode.org/wiki/Strip_block_comments",
        "http://rosettacode.org/wiki/Substring/Top_and_tail", "http://rosettacode.org/wiki/Sutherland-Hodgman_polygon_clipping", "http://rosettacode.org/wiki/Terminal_control/Ringing_the_terminal_bell",
        "http://rosettacode.org/wiki/Textonyms", "http://rosettacode.org/wiki/Thiele%27s_interpolation_formula", "http://rosettacode.org/wiki/Time_a_function",
        "http://rosettacode.org/wiki/Trabb_Pardo%E2%80%93Knuth_algorithm", "http://rosettacode.org/wiki/Tree_traversal", "http://rosettacode.org/wiki/URL_encoding",
        "http://rosettacode.org/wiki/Variable-length_quantity", "http://rosettacode.org/wiki/Verify_distribution_uniformity/Chi-squared_test", "http://rosettacode.org/wiki/Verify_distribution_uniformity/Naive",
        "http://rosettacode.org/wiki/Zebra_puzzle", "http://rosettacode.org/wiki/Zhang-Suen_thinning_algorithm" ]

n=0
for y in range(0, len(URL)):
    # Realizamos la petición a la web
    req = requests.get(URL[y])

    # Comprobamos que la petición nos devuelve un Status Code = 200
    status_code = req.status_code
    if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        lista=['python','ada', 'algol68', 'awk', 'text',
                'c', 'csharp', 'clojure', 'd',
                'erlang', 'go', 'haskell',
                'icon', 'java', 'javascript', 'scala',
                'lua', 'perl', 'perl6', 'powershell',
                'prolog', 'purebasic', 
                'ruby', 'tcl', 'bash', 'zxbasic']
        # Obtenemos todos los divs donde están las entradas
        
        for x in range(0, len(lista)):
            entradas = html.find_all('pre', {'class': lista[x]+' highlighted_source'})

            i=''.join(str(e) for e in entradas)
            cleantext = BeautifulSoup(i, "lxml").text
            if cleantext=="":
                print("archivo vacio")
            else:
                try:
                    archivo= open("zop"+str(n)+".txt","w")
                    archivo.write(cleantext)
                    print("archivo realizado")
                    archivo.close()
                    n=n+1
                except ValueError:
                    print("no se pudo")
     # Recorremos todas las entradas para extraer el título, autor y fecha


    else:
        print ("Status Code %d" % status_code)
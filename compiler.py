from eight_to_ten import eight_to_ten as ette
from fib import fibonacci
from fib import ten_to_fib as ttf
from morze import morse as m
from three_to_eight import three_to_eight as thte


def main(n):
    text = "0) " + str(n) + "\n" # full steps of the compiling
    n, err = m(n)
    if err:
        print(f'Found error: {err}')
        return(f'Found error: {err}')
    else:
        text += "1) " + str(n) + " (from symbols to three/morze)\n"
        n, err = thte(n)
        if err:
            print(f'Found error: {err}')
            return(f'Found error: {err}')
        else:
            text += "2) " + str(n) + " (from three/morze to eight)\n"
            n, err = ette(n)
            if err:
                print(f'Found error: {err}')
                return(f'Found error: {err}')
            else:
                text += "3) " + str(n) + " (from eight to ten)\n"
                n, err = ttf(n)
                if err:
                    print(f'Found error: {err}')
                    return(f'Found error: {err}')
                else:
                    text += "4) " + str(n) + " (from ten to fibonacci)"
                    print(text)
                    return(text)

if __name__ == '__main__':
    main("20000")

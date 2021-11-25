from reversemorse import morse as rm
from ten_to_eight import ten_to_eight as tte
from fib_to_ten import fib_to_ten as ftt
from eight_to_three import eight_to_three as etth

def main(n):
    text = "0) " + str(n) + "\n"  # full steps of the decompiling
    n, err = ftt(n)
    if err:
        print(f'Found error: {err}')
        return(f'Found error: {err}')
    else:
        text += "1) " + str(n) + " (from fibonacci to ten)\n"
        n, err = tte(n)
        if err:
            print(f'Found error: {err}')
            return(f'Found error: {err}')
        else:
            text += "2) " + str(n) + " (from ten to eight)\n"
            n, err = etth(n)
            if err:
                print(f'Found error: {err}')
                return(f'Found error: {err}')
            else:
                text += "3) " + str(n) + " (from eight to three/morze)\n"
                n, err = rm(n)
                if err:
                    print(f'Found error: {err}')
                    return(f'Found error: {err}')
                else:
                    text += "4) " + "".join(n) + " (from three/morze to symbols)"
                    print(text)
                    return n


if __name__ == '__main__':
    main("010100001001010010100010101010100010100000100000101001010100000100100101000010000100001000010100100100")

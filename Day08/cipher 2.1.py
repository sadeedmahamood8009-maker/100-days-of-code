alplabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
text = input("Enter the text\n").lower()
shift = int(input("Enter the shift number\n"))

def caeser(original_text,shift_amount,encode_or_decode):
    cipher_text = "" 
    for i in original_text:
      if encode_or_decode == "decode":
        shift_amount *= -1

      shifted_position = alplabet.index(i) + shift_amount
      shifted_position = shifted_position % len(alplabet)
      cipher_text += alplabet[shifted_position]
    print(f"here is the {encode_or_decode}d result :{cipher_text}")
caeser(original_text=text,shift_amount=shift,encode_or_decode=direction)
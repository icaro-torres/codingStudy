package com.loiane.cursojava.aula13;

public class OperadoresAritmeticos {
    public static void main(String[] args) {

        int resultado = 1 + 2;
        System.out.println(resultado);

        resultado = resultado - 1;
        System.out.println(resultado);

        resultado = resultado * 5;
        System.out.println(resultado);

        resultado = resultado / 2;
        System.out.println(resultado);

        resultado = resultado + 8;
        System.out.println(resultado);

        resultado = resultado % 7;
        System.out.println(resultado);

        String primeiroNome = "Esta é";
        String secundoNome = " uma String concatenada";
        String terceiroNome = primeiroNome + secundoNome;
        System.out.println(terceiroNome);

        // também dá pra fazer resultado += 1;
        resultado = resultado + 1;
        System.out.println(resultado);

        resultado++;
        System.out.println(resultado);

        System.out.println(resultado++); // aqui imprime o valor para depois adicionar
        System.out.println(++resultado); // aqui ele já adiciona antes de imprimir

        resultado--;
        System.out.println(resultado);

        System.out.println(resultado--);
        System.out.println(--resultado);
    }
}

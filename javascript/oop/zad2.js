
function doWelcome() {
    return "Hello";
    
}

console.log(doWelcome());


// 2. Напиши функцию, которая принимает имя пользователя и
//  возвращает новую строку с персональным приветствием.

function getUserWelcome(name) {
    return `Hello ${name}`;  // шаблонный литерал 
}

console.log(getUserWelcome("Nata"));


// 3. Напиши функцию, которая принимает текущий год и год рождения,
//  а затем вычисляет и возвращает возраст.

function getAge(currentYear, yearBirth) {
    return currentYear - yearBirth;
}

console.log(getAge(2026, 2000));

// 4. Напиши функцию, которая принимает два числа и возвращает 
// результат вычитания второго из первого.

function Subtract(number1, number2) {
    return number2 - number1;
}

console.log(Subtract(879, 545));
console.log(Subtract(345, 878));

// 5. Напиши функцию, которая принимает одно число, 
// умножает его само на себя и возвращает этот результат.

function multiply(number1) {
    return number1 * number1;
}

console.log(multiply(5));


// 6. Напиши функцию, которая принимает отдельные строки с именем
//  и фамилией, а возвращает их склеенными в одну строку через пробел.

function glue(name, surname) {
    return name + surname;
}

console.log(glue("nata", "ivano"));



// 7. Напиши функцию, которая принимает любое логическое значение и 
// возвращает строго противоположное ему.

function invert(value) {
    return !value;
}

console.log(invert(true));


// 8. Напиши функцию, которая принимает число и через условие
//  возвращает истину, если оно больше нуля, и ложь в противном случае.

function confirmation(number) {
    if (number > 0) {
        return true;
    }

    else 
        return false;
}

console.log(confirmation(20));


// 9. Напиши две функции: первая их них принимает возраст и возвращает true, 
// если он достиг совершеннолетия, и false, если нет, а вторая возвращает строку
// "совершеннолетний", если совершеннолетний, иначе "несовершеннолетний".
//  Вторая функция должна использовать первую.

function checkAdult(age) {
    return age >= 18
}    
function getAdultStatus(age) {
    if (checkAdult(age)) {
        return "совершеннолетний";
    }
    else 
        return "несовершеннолетний";
} 


console.log(getAdultStatus(19));






// 10.Напиши функцию, которая принимает два числа и с помощью простого
//  условия определяет и возвращает наибольшее из них.

function max(number1, number2) {
    if (number1 > number2) {
        return number1;
    }
    return number2;
}

console.log(max(21, 15));


// 11.Напиши функцию, которая принимает три разных числа, складывает 
// их и возвращает среднее арифметическое значение.

function getArithmeticMean(num1, num2, num3) {
    return (num1 + num2 + num3)/3;
}

console.log(getArithmeticMean(100, 200, 300));


// 12. Напиши функцию, которая принимает исходную цену товара и
//  процент скидки, вычисляет и возвращает итоговую стоимость.

// function finalCost(originalPriceOfProduct, discountPercentage) {  
    

// }





// возвращает это же значение, переведенное в метры.



// 17.Напиши функцию, которая принимает число и с помощью цикла выводит в
//  консоль все четные числа от единицы до этого числа.

function printEvenNumbers(number) {
    for (let i = 1; i <= number; i++) {
        if (i % 2 === 0) {
        console.log(i);    
        }
    }
}

printEvenNumbers(10);


// 32.Создай функцию Питомец, которая принимает кличку 
// и вид животного, и имеет метод, выводящий в консоль информацию о нем.

function pet()
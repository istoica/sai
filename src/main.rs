use std::env;
use std::io::{self, Read};
use std::process;

fn quick_sort(arr: &[f64]) -> Vec<f64> {
    if arr.len() <= 1 {
        return arr.to_vec();
    }

    let pivot = arr[arr.len() / 2];
    let left: Vec<f64> = arr.iter().copied().filter(|x| *x < pivot).collect();
    let middle: Vec<f64> = arr.iter().copied().filter(|x| *x == pivot).collect();
    let right: Vec<f64> = arr.iter().copied().filter(|x| *x > pivot).collect();

    let mut result = quick_sort(&left);
    result.extend(middle);
    result.extend(quick_sort(&right));
    result
}

fn parse_numbers(input: &[String], source_name: &str) -> Vec<f64> {
    let mut numbers = Vec::new();
    for token in input {
        match token.parse::<f64>() {
            Ok(num) => numbers.push(num),
            Err(_) => {
                eprintln!("Error: All {} must be valid numbers", source_name);
                process::exit(1);
            }
        }
    }
    numbers
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();

    let numbers = if !args.is_empty() {
        parse_numbers(&args, "arguments")
    } else {
        println!("Enter numbers separated by spaces or newlines (Ctrl+D to finish):");
        let mut input_text = String::new();
        if let Err(err) = io::stdin().read_to_string(&mut input_text) {
            eprintln!("Error reading from stdin: {}", err);
            process::exit(1);
        }

        let tokens: Vec<String> = input_text
            .split_whitespace()
            .map(|s| s.to_string())
            .collect();
        parse_numbers(&tokens, "inputs")
    };

    if numbers.is_empty() {
        eprintln!("Error: No numbers provided");
        process::exit(1);
    }

    let sorted_numbers = quick_sort(&numbers);

    for num in sorted_numbers {
        if num.fract() == 0.0 {
            println!("{:.0}", num);
        } else {
            println!("{}", num);
        }
    }
}

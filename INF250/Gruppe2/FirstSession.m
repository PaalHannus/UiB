
a = [1 2 3];
b = 2;


for i = 1:10
    disp("Lucasnumber:")
    disp(lucasnumbers(i));
end


function [lucas_numbers] = lucasnumbers(In)
    if (In == 1)
        lucas_numbers = 2;
    elseif (In == 2)
        lucas_numbers = 1;
    else
        lucas_numbers = (lucasnumbers(In - 1) + lucasnumbers(In - 2));
        
    end
end



{# 
This macro returns the description of the payment payment_type_description #}


{% macro get_payment_type_description -%}

    case (( payment_type ))
        when 1 then 'Credit card'
        when 2 then 'Cash'
        when 3 then 'No charge'
        when 4 then 'Dispute'
        when 5 then 'Unknown'
        when 6 then 'Voided trip'
    end

{%- endmacro %}
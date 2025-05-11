
PORCENTAJE_TSS = 0.0304  # 3.04% del sueldo bruto

# Definición de rangos para el ISR (anual)
RANGO_EXENTO_ANUAL = 416220  # Hasta RD$416,220 (exento)
RANGO_MEDIO1_ANUAL = 624329  # Hasta RD$624,329 (15% del excedente)
RANGO_MEDIO2_ANUAL = 867123  # Hasta RD$867,123 (20% del excedente + monto fijo)
# Más de RD$867,123 (25% del excedente + monto fijo)

# Montos IRS
MONTO_FIJO_RANGO_MEDIO2 = 31216  # RD$31,216
MONTO_FIJO_RANGO_ALTO = 79776  # RD$79,776


PORCENTAJE_BONIFICACION = 0.0833  

def calcular_isr(sueldo_mensual):
    
    # Convertir el sueldo mensual a anual para calcular el ISR
    sueldo_anual = sueldo_mensual * 12
    
    # Determinar el ISR según el rango de ingresos
    if sueldo_anual <= RANGO_EXENTO_ANUAL:
        # Exento de ISR
        isr_anual = 0
    elif sueldo_anual <= RANGO_MEDIO1_ANUAL:
        # 15% del excedente sobre RD$416,220
        excedente = sueldo_anual - RANGO_EXENTO_ANUAL
        isr_anual = excedente * 0.15
    elif sueldo_anual <= RANGO_MEDIO2_ANUAL:
        # RD$31,216 + 20% del excedente sobre RD$624,329
        excedente = sueldo_anual - RANGO_MEDIO1_ANUAL
        isr_anual = MONTO_FIJO_RANGO_MEDIO2 + (excedente * 0.20)
    else:
        # RD$79,776 + 25% del excedente sobre RD$867,123
        excedente = sueldo_anual - RANGO_MEDIO2_ANUAL
        isr_anual = MONTO_FIJO_RANGO_ALTO + (excedente * 0.25)
    
    # Dividir el ISR anual entre 12 para obtener la retención mensual
    isr_mensual = isr_anual / 12
    return isr_mensual

def main():

    print("===== CALCULADORA DE SUELDO NETO EN REPÚBLICA DOMINICANA =====")
    
    while True:
        try:
            sueldo_bruto = float(input("\nIntroduzca el sueldo bruto mensual (RD$): "))
            if sueldo_bruto <= 0:
                print("Error: El sueldo bruto debe ser un valor positivo.")

            else:
                    break
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")

    # Solicitar otros descuentos 
    while True:
        try:
            otros_descuentos = float(input("Introduzca otros descuentos adicionales (RD$) [0 si no hay]: "))
            if otros_descuentos < 0:
                print("Error: Los descuentos no pueden ser negativos.")
            else:
                break
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")
    
    # Calcular descuento por Seguridad Social (TSS)
    descuento_tss = sueldo_bruto * PORCENTAJE_TSS
    
    # Calcular retención de ISR
    retencion_isr = calcular_isr(sueldo_bruto)
    
    # Calcular bonificación
    bonificacion = sueldo_bruto * PORCENTAJE_BONIFICACION
    
    # Calcular sueldo neto
    sueldo_neto = sueldo_bruto - descuento_tss - retencion_isr - otros_descuentos + bonificacion
    
    # Mostrar resultados
    print("\n===== RESULTADOS =====")
    print(f"Sueldo Bruto: RD$ {sueldo_bruto:.2f}")
    print(f"Descuento por Seguridad Social (TSS - 3.04%): RD$ {descuento_tss:.2f}")
    print(f"Retención ISR: RD$ {retencion_isr:.2f}")
    print(f"Otros Descuentos: RD$ {otros_descuentos:.2f}")
    print(f"Bonificación (8.33%): RD$ {bonificacion:.2f}")
    print(f"SUELDO NETO: RD$ {sueldo_neto:.2f}")
    
    print("\nDesglose de descuentos y bonificación:")
    print(f"- Total descuentos: RD$ {descuento_tss + retencion_isr + otros_descuentos:.2f}")
    print(f"- Total bonificaciones: RD$ {bonificacion:.2f}")

if __name__ == "__main__":
    main()
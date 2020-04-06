from src.dco.ApDcoOlx import ApDco

a = ApDco()
aptos = a.get_results()
a.write_results(aptos)

import pandas as pd

df_p1 = pd.DataFrame({'Branche': ['IKT', 'Finanzdienstleistungen', 'B2B Dienstleistungen', 'Elektrotechnik/ Maschinenbau',
                                  'Fahrzeugbau', 'Chemie/Ph., Gr.st.', 'Ver-/Entsorg., Bg.b.', 'Sonst. Verarb. Gew.', 'Sonst. Dienstleist.',
                                  'Verkehr, Logistik', 'Großhandel'],
                      'Anteil': [0.178, 0.122, 0.111, 0.068, 0.051, 0.046, 0.036, 0.033, 0.025, 0.015, 0.01]})

df_p2 = pd.DataFrame({'Branche': ['IKT', 'Finanzdienstleistungen', 'B2B Dienstleistungen', 'Elektrotechnik/ Maschinenbau',
                                  'Fahrzeugbau', 'Chemie/Ph., Gr.st.', 'Ver-/Entsorg., Bg.b.', 'Sonst. Verarb. Gew.', 'Sonst. Dienstleist.',
                                  'Verkehr, Logistik', 'Großhandel'],
                      'Umsatz': [0.033, 0.03, 0.021, 0.013, 0.006, 0.007, 0.008, 0.009, 0.005, 0.005, 0.004],
                      'Ausgaben': [0.0056, 0.0004, 0.0029, 0.0017, 0.0016, 0.0003, 0.0001, 0.0004, 0.0012, 0.0006, 0.0001],
                      ' ': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})

df_p3 = pd.DataFrame({'Unternehmen': ['KI-Entwickler', 'KI-Berater', 'KI-Anwender', 'KI-Startups (alle)', 'alle Gründungen'],
                      'aktiv': [0.93, 0.93, 0.88, 0.92, 0.45],
                      'vermutlich stillgelegt': [0.02, 0.02, 0.04, 0.03, 0.19],
                      'geschlossen': [0.05, 0.06, 0.07, 0.06, 0.36]})

df_p4 = pd.DataFrame({'y': ['Marketing', 'Produktion & Instandhaltung', 'Kundendienst', 'Vertrieb', 'Bereichsübergreifend (Texte)',
                      'Buchaltung', 'Managementunterstützung', 'IT-Abteilung', 'Logistik', 'Forschung & Entwicklung', 'Personalabteilung',
                      'Controlling', 'Rechts- & Steuerabteilung'],
                      'Anteil': [0.71, 0.64, 0.63, 0.53, 0.50, 0.44, 0.43, 0.39, 0.35, 0.25, 0.21, 0.18, 0.01]})

df_p5 = pd.DataFrame({'Faktor': ['Verbesserung der IT Ausstattung',
                                 'Staatliche finanzielle Förderung',
                                 'Datenschutzkonforme Cloud-Angebote',
                                 'Vertrauen von Nutzern und Anwendern',
                                 'Umfassendere Information der Öffentlichkeit',
                                 'Verfügbarkeit großer, öffentlicher Datenmengen',
                                 'Mehr KI-Weiterbildungsangebote',
                                 'Datenschutzanpassungen',
                                 'Größeres Angebot an KI-Fachkräften'],
                      'stark': [0.46, 0.44, 0.43, 0.36, 0.27, 0.26, 0.24, 0.21, 0.17],
                      'weniger stark': [0.24, 0.27, 0.23, 0.35, 0.34, 0.40, 0.34, 0.34, 0.39],
                      'gar nicht': [0.30, 0.29, 0.34, 0.29, 0.39, 0.34, 0.41, 0.44, 0.44]})
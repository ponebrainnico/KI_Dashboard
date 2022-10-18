import pandas as pd

df_p1 = pd.DataFrame({'Branche': ['IKT', 'Finanzdienstleistungen', 'Unternehmensnahe Dienstleistungen', 'Elektrotechnik/Maschinenbau',
                                  'Fahrzeugbau', 'Chemie/Ph., Gr.st.', 'Ver-/Entsorg., Bg.b.', 'Sonst. Verarb. Gew.', 'Sonst. Dienstleist.',
                                  'Verkehr, Logistik', 'Großhandel'],
                      'Anteil': [17.8, 12.2, 11.1, 6.8, 5.1, 4.6, 3.6, 3.3, 2.5, 1.5, 1]})

df_p2 = pd.DataFrame({'Branche': ['IKT', 'Finanzdienstleistungen', 'Unternehmensnahe Dienstleistungen', 'Elektrotechnik/Maschinenbau',
                                  'Fahrzeugbau', 'Chemie/Ph., Gr.st.', 'Ver-/Entsorg., Bg.b.', 'Sonst. Verarb. Gew.', 'Sonst. Dienstleist.',
                                  'Verkehr, Logistik', 'Großhandel'],
                      'Anteil Umsatz': [3.3, 3, 2.1, 1.3, 0.6, 0.7, 0.8, 0.9, 0.5, 0.5, 0.4],
                      'Anteil Ausgaben': [0.56, 0.04, 0.29, 0.17, 0.16, 0.03, 0.01, 0.04, 0.12, 0.06, 0.01],
                      ' ': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})

df_p3 = pd.DataFrame({'Unternehmen': ['KI-Entwickler', 'KI-Berater', 'KI-Anwender', 'KI-Startups insgesamt', 'alle Gründungen'],
                      'aktiv': [93, 93, 88, 92, 45],
                      'vermutlich stillgelegt': [2, 2, 4, 3, 19],
                      'geschlossen': [5, 6, 7, 6, 36]})

df_p4 = pd.DataFrame({'Unternehmensbereich': ['Marketing', 'Produktion und Instandhaltung', 'Kundendienst', 'Vertrieb', 'Bereichsübergreifend bei Texten o. Übersetzungen',
                      'Buchaltung', 'Managementunterstützung bei der Strategieentwicklung', 'IT-Abteilung', 'Logistik', 'Forschung und Entwicklung', 'Personalabteilung',
                      'Controlling', 'Rechts- und Steuerabteilung'],
                      'Anteil': [71, 64, 63, 53, 50, 44, 43, 39, 35, 25, 21, 18, 1]})

df_p5 = pd.DataFrame({'Faktor': ['Verbesserung der technischen Ausstattung im Bereich IT',
                                 'Staatliche finanzielle Förderung',
                                 'Datenschutzkonforme Cloud-Angebote',
                                 'Vertrauen von Nutzern und Anwendern in KI',
                                 'Umfassendere Information der Öffentlichkeit über KI und dessen Nutzen',
                                 'Verfügbarkeit großer Datenmengen aus öffentlichen Quellen',
                                 'Mehr Weiterbildungsangebote zum Thema KI',
                                 'Anpassung des Datenschutzen, um KI-basierte Analysen zu erleichtern',
                                 'Größeres Angebot an Fachkräften mit KI-Kompetenzen'],
                      'stark': [46, 44, 43, 36, 27, 26, 24, 21, 17],
                      'weniger stark': [24, 27, 23, 35, 34, 40, 34, 34, 39],
                      'gar nicht': [30, 29, 34, 29, 39, 34, 41, 44, 44]})
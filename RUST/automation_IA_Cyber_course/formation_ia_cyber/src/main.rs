use std::io;

struct Cours {
    titre: String,
    niveau: String,
    duree: String,
}

fn afficher_cours(domaine: &str, cours: Vec<Cours>) {
    println!("\nCours recommandés en {} :", domaine);

    for c in cours {
        println!("--------------------------");
        println!("Titre  : {}", c.titre);
        println!("Niveau : {}", c.niveau);
        println!("Durée  : {}", c.duree);
    }
}

fn main() {
    println!("=== Plateforme de recommandation de compétences ===");
    println!("Choisissez un domaine :");
    println!("1. Intelligence Artificielle");
    println!("2. Cybersécurité");

    let mut choix = String::new();

    io::stdin()
        .read_line(&mut choix)
        .expect("Erreur de lecture");

    let choix = choix.trim();

    if choix == "1" {
        let cours_ia = vec![
            Cours {
                titre: String::from("Introduction à l'IA"),
                niveau: String::from("Débutant"),
                duree: String::from("2 semaines"),
            },
            Cours {
                titre: String::from("Machine Learning avec Python"),
                niveau: String::from("Intermédiaire"),
                duree: String::from("4 semaines"),
            },
            Cours {
                titre: String::from("Deep Learning et réseaux de neurones"),
                niveau: String::from("Avancé"),
                duree: String::from("6 semaines"),
            },
        ];

        afficher_cours("Intelligence Artificielle", cours_ia);
    } else if choix == "2" {
        let cours_cyber = vec![
            Cours {
                titre: String::from("Bases de la cybersécurité"),
                niveau: String::from("Débutant"),
                duree: String::from("2 semaines"),
            },
            Cours {
                titre: String::from("Sécurité réseau"),
                niveau: String::from("Intermédiaire"),
                duree: String::from("4 semaines"),
            },
            Cours {
                titre: String::from("Ethical Hacking"),
                niveau: String::from("Avancé"),
                duree: String::from("6 semaines"),
            },
        ];

        afficher_cours("Cybersécurité", cours_cyber);
    } else {
        println!("Choix invalide. Veuillez choisir 1 ou 2.");
    }
}
